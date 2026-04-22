# Linux Basics Assignment

## Objective
This assignment demonstrates basic Linux commands related to file management, searching, compression, downloading files, permissions, and environment variables.

---

## 1. Creating and Renaming Files/Directories

### Commands
```bash
mkdir test_dir
touch test_dir/example.txt
mv test_dir/example.txt test_dir/renamed_example.txt
```

### Explanation
- `mkdir` creates a directory.
- `touch` creates an empty file.
- `mv` renames the file.

---

## 2. Viewing File Contents

### Commands
```bash
cat /etc/passwd
head -5 /etc/passwd
tail -5 /etc/passwd
```

### Explanation
- `cat` displays file contents.
- `head -5` shows first five lines.
- `tail -5` shows last five lines.

---

## 3. Searching for Patterns

### Command
```bash
grep "root" /etc/passwd
```

### Explanation
Searches for lines containing "root".

---

## 4. Zipping and Unzipping

### Commands
```bash
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
```

### Explanation
Compresses and extracts a directory.

---

## 5. Downloading Files

### Command
```bash
wget -O sample.txt https://www.gnu.org/licenses/gpl-3.0.txt
```

### Explanation
Downloads a sample text file from the internet.

---

## 6. Changing Permissions

### Commands
```bash
touch secure.txt
chmod 444 secure.txt
ls -l secure.txt
```

### Explanation
Makes the file read-only for everyone.

---

## 7. Working with Environment Variables

### Commands
```bash
export MY_VAR=Hello,\ Linux!
echo $MY_VAR
```

### Output
```bash
Hello, Linux!
```

---

## Repository Contents
- README.md
- Screenshots folder (optional)
- Assignment document (optional)

---

## Conclusion
This assignment helped practice essential Linux commands for day-to-day administration tasks.


