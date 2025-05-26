# Problema celor n regine

Urmați pașii de mai jos pentru a crea și activa un mediu virtual Python:

## 1. Crearea unui mediu virtual
1. Deschideți terminalul sau linia de comandă.
2. Navigați la directorul proiectului:
    ```bash
    cd /calea/catre/proiect
    ```
3. Creați un mediu virtual utilizând comanda:
    ```bash
    python -m venv nume_env
    ```
    sau
    ```bash
    python3 -m venv nume_env
    ```
## 2. Activarea mediului virtual
- **Pe Windows**:
  ```bash
  .\env\Scripts\activate
  ```
Este posibil sa apara urmatoarea eroare:
```bash
nume_env\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this     
system.
```
In acest caz se poate rula urmatoarea comanda can vrem sa activam env-ul:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
- **Pe macOS/Linux**:
  ```bash
  source env/bin/activate
  ```

După activare, ar trebui să vedeți numele mediului virtual (ex. `(env)`) înaintea promptului terminalului.

## 3. Dezactivarea mediului virtual
Pentru a dezactiva mediul virtual, utilizați comanda:
```bash
deactivate
```

## 4. Instalarea pachetelor necesare
După activare, puteți instala pachetele specificate în fișierul `requirements.txt` utilizând comanda:
```bash
pip install -r requirements.txt
```

## 5. Salvarea dependențelor
Pentru a salva dependențele într-un fișier `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## Structura proiectului

Proiectul este organizat în următoarele fișiere și directoare:

### 1. `main.py`
- Acesta este punctul de intrare al aplicației.
- Conține logica principală pentru rezolvarea problemei celor n regine.
- Apelează funcțiile definite în alte module pentru a genera soluții.

### 2. `backtracking.py`
- Aici este implementata rezolvarea problemei utilizand algoritmul backtracking

### 3. `hill_climbing.py`
Aici este implementata rezolvarea problemei utilizand algoritmul hill_climbing



### 4. `README.md`
- Documentația proiectului, care explică cum să configurați mediul, să rulați aplicația și să înțelegeți structura proiectului.