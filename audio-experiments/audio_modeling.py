import os
import numpy as np
import librosa
import torch
import torch.nn as nn
import torch.optim as optim
import torchaudio
from torch.utils.data import Dataset, DataLoader

def extract_spectrogram(wav_file, n_mels=64, n_fft=1024, hop_length=512):
    """
    Converts a WAV audio file into a mel spectrogram (2D array).
    """
    y, sr = librosa.load(wav_file, sr=None)  # Loads with native sampling rate
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, 
                                                 n_fft=n_fft, 
                                                 hop_length=hop_length)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    return spectrogram_db

class AudioDataset(Dataset):
    def __init__(self, data_dir, phrases, transform=None):
        self.data_dir = data_dir
        self.phrases = phrases
        self.transform = transform

        # Create a label map and file list
        self.label_map = {phrase: idx for idx, phrase in enumerate(phrases)}
        self.file_list = []
        self.label_list = []

        # Populate the file and label lists
        for phrase in phrases:
            files = [f for f in os.listdir(data_dir) 
                     if f.startswith(phrase.replace(' ', '_')) and f.endswith('.wav')]
            for file in files:
                self.file_list.append(os.path.join(data_dir, file))
                self.label_list.append(self.label_map[phrase])

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        wav_path = self.file_list[idx]
        label = self.label_list[idx]

        spec = extract_spectrogram(wav_path)  # shape: (n_mels, time_frames)
        # Expand dims to (1, n_mels, time_frames) so PyTorch treats it like a single channel
        spec = np.expand_dims(spec, axis=0)
        
        # Optional transform (e.g., normalization) if desired
        if self.transform:
            spec = self.transform(spec)

        # Convert to PyTorch tensors
        spec_tensor = torch.tensor(spec, dtype=torch.float)
        label_tensor = torch.tensor(label, dtype=torch.long)

        return spec_tensor, label_tensor

class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Global pooling that collapses all height/width to 1x1
        self.global_pool = nn.AdaptiveAvgPool2d((1, 1))

        # Now the input to fc1 will be 32 * 1 * 1 = 32
        self.fc1 = nn.Linear(32, 64)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # (B,16,mel/2,time/2)
        x = self.pool(torch.relu(self.conv2(x)))  # (B,32,mel/4,time/4)

        # This collapses each channel’s 2D map into a single number
        x = self.global_pool(x)                   # (B,32,1,1)
        x = x.view(x.size(0), -1)                 # (B,32)

        x = torch.relu(self.fc1(x))               # (B,64)
        x = self.fc2(x)                           # (B,num_classes)
        return x


def train_model(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    correct = 0
    for specs, labels in train_loader:
        specs, labels = specs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(specs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        predicted = torch.argmax(outputs, dim=1)
        correct += (predicted == labels).sum().item()

    avg_loss = total_loss / len(train_loader)
    accuracy = correct / len(train_loader.dataset)
    return avg_loss, accuracy

def evaluate_model(model, val_loader, criterion, device):
    model.eval()
    total_loss = 0
    correct = 0
    with torch.no_grad():
        for specs, labels in val_loader:
            specs, labels = specs.to(device), labels.to(device)
            outputs = model(specs)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            predicted = torch.argmax(outputs, dim=1)
            correct += (predicted == labels).sum().item()
    avg_loss = total_loss / len(val_loader)
    accuracy = correct / len(val_loader.dataset)
    return avg_loss, accuracy

def main():
    data_dir = "recordings"  # Path to your recordings
    phrases = [
        "Sunka",
        "Wanbli",
        "Mato",
        "Sunka Wakan",
        "Wakiyan",
        # Add more phrases as needed
    ]

    # Create dataset and split into train/val
    full_dataset = AudioDataset(data_dir, phrases)
    num_items = len(full_dataset)
    split_idx = int(0.8 * num_items)  # 80% for train, 20% for validation
    train_dataset, val_dataset = torch.utils.data.random_split(
        full_dataset, [split_idx, num_items - split_idx]
    )

    batch_size = 8
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    num_classes = len(phrases)
    model = SimpleCNN(num_classes)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    epochs = 10
    for epoch in range(epochs):
        train_loss, train_acc = train_model(model, train_loader, criterion, optimizer, device)
        val_loss, val_acc = evaluate_model(model, val_loader, criterion, device)
        print(f"Epoch [{epoch+1}/{epochs}] "
              f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f} | "
              f"Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.4f}")
        
    # Save model to my_audio_model.pth
    torch.save(model.state_dict(), "my_audio_model.pth")

if __name__ == "__main__":
    main()
