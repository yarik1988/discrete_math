## Environment & Shell Setup

* **WSL Distribution:** Ubuntu
* **Conda Environment:** `sage`
* **Default Shell Launch Command:**
  ```bash
  wsl.exe -d Ubuntu -e bash -c "bash --rcfile <(echo 'source ~/.bashrc; conda activate sage')"