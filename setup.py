from setuptools import setup, find_packages

setup(
    name="StyleTTS2",
    version="0.0.1",
    description="StyleTTS2 text-to-speech synthesis system",
    packages=find_packages(),
    install_requires=[
        "SoundFile",
        "torchaudio",
        "munch",
        "torch",
        "pydub",
        "pyyaml",
        "librosa",
        "nltk",
        "matplotlib",
        "accelerate",
        "transformers",
        "einops",
        "einops-exts",
        "tqdm",
        "typing",
        "typing-extensions",
    ],
    dependency_links=[
        "git+https://github.com/resemble-ai/monotonic_align.git#egg=monotonic_align"
    ],
    entry_points={
        "console_scripts": [
            "styletts2=style_tts2_pipeline:main",
        ],
    },
) 