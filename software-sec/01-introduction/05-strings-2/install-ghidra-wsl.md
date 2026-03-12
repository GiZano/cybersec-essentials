# 1. Install OpenJDK

```bash
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt install openjdk-21-jdk
```

# 2. Install Ghidra

## 2.1 Get the zip

> Get the zip url at ```https://github.com/NationalSecurityAgency/ghidra/releases```

```bash
wget <ZIP_URL>
```

## 2.2 Extract the archive

### Install Unzipper if not yet present

```bash
sudo apt update && sudo apt install unzip
```

### Extract

```bash
unzip ghidra_*.zip
```

# 3. Run Ghidra

## 