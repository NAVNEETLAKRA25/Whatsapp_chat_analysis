from setuptools import setup, find_packages

setup(
    name="whatsapp-chat-analyzer",
    version="0.1.0",
    description="A WhatsApp chat analysis tool for text preprocessing, EDA, and visualization.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas==2.2.2",
        "matplotlib==3.9.2",
        "numpy==1.26.4",
        "regex==2024.5.15",
        "nltk==3.9.1"
    ],
    python_requires=">=3.9",
)
