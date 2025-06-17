# Use a base image that supports CUDA and cuDNN
FROM nvcr.io/nvidia/pytorch:24.02-py3

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Denver

# Install OS packages
RUN apt-get update && apt-get install -y \
    git \
    pandoc \
    texlive-xetex \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Upgrade pip and install Python packages
RUN pip install --no-cache-dir --upgrade pip \
        fastai==2.7.12 \
        numpy==1.24.4 \
        pandas==1.5.3 \
        matplotlib==3.7.1 \
        nbdev \
        gradio \
        jupyter \
        timm

# Clean up NVIDIA sample files (corrected to /workspace)
RUN rm -rf /workspace/docker-examples \
           /workspace/examples \
           /workspace/tutorials \
           /workspace/README.md \
           /workspace/NVIDIA_Deep_Learning_Container_License.pdf

# Expose Jupyter notebook port
EXPOSE 8888

# Set the working directory in the container
WORKDIR /workspace

# Create a directory for persisting data
ADD notebooks /workspace/notebooks/.
ADD data /workspace/data/.
ADD images /workspace/images/.
ADD models /workspace/models/.

# Start Jupyter notebook when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/workspace", "--NotebookApp.use_redirect_file=False", "--NotebookApp.custom_display_url=http://localhost:8888"]
