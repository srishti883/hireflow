# Python & Django Terminal Guide

## Part 1: Open Terminal in VS Code

### **Method 1: Keyboard Shortcut (Fastest)**
```
Press: Ctrl + ` (backtick)
```
- Opens/closes terminal at the bottom

### **Method 2: Using Menu**
```
Click: View → Terminal
```

### **Method 3: Command Palette**
```
Press: Ctrl + Shift + P
Type: Toggle Integrated Terminal
Press: Enter
```

---

## Part 2: Navigate to Your Django Project

### **Step 1: Open Terminal**
Press `Ctrl + `` to open terminal

### **Step 2: Navigate to Backend Folder**
```powershell
Set-Location "C:\Users\Srishti\Desktop\hireFlow\bckend"
```

Or use `cd` command:
```cmd
cd C:\Users\Srishti\Desktop\hireFlow\bckend
```

### **Step 3: Verify You're in Correct Folder**
```powershell
Get-Location
```
Should show: `C:\Users\Srishti\Desktop\hireFlow\bckend`

---

## Part 3: Run Django Development Server

### **Option 1: Full Path (Works Anywhere)**
```powershell
& "venv\Scripts\python.exe" manage.py runserver
```

### **Option 2: Short Command (After Activation)**
First activate virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

Then run:
```powershell
python manage.py runserver
```

### **Server Output Example**
```
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
Django version 6.0.7, using settings 'hireflow_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### **Access Server**
Open browser and go to: `http://127.0.0.1:8000/`

### **Stop Server**
Press: `Ctrl + C` (or `Ctrl + Break` on some keyboards)

---

## Part 4: Common Python & Django Commands

### **Check Python Version**
```powershell
& "venv\Scripts\python.exe" --version
```

### **Check Installed Packages**
```powershell
& "venv\Scripts\python.exe" -m pip list
```

### **Install a Package**
```powershell
& "venv\Scripts\python.exe" -m pip install package_name
```

### **Django System Check**
```powershell
& "venv\Scripts\python.exe" manage.py check
```

### **Create Django Migrations**
```powershell
& "venv\Scripts\python.exe" manage.py makemigrations
```

### **Apply Migrations**
```powershell
& "venv\Scripts\python.exe" manage.py migrate
```

### **Create Superuser (Admin)**
```powershell
& "venv\Scripts\python.exe" manage.py createsuperuser
```

### **Django Shell (Python REPL)**
```powershell
& "venv\Scripts\python.exe" manage.py shell
```

### **Collect Static Files**
```powershell
& "venv\Scripts\python.exe" manage.py collectstatic
```

### **Show Migration Status**
```powershell
& "venv\Scripts\python.exe" manage.py showmigrations
```

### **Create New App**
```powershell
& "venv\Scripts\python.exe" manage.py startapp app_name
```

---

## Part 5: Quick Start Workflow

### **Complete Startup Steps:**

```powershell
# Step 1: Open terminal (Ctrl + `)
# Already open!

# Step 2: Navigate to backend folder
Set-Location "C:\Users\Srishti\Desktop\hireFlow\bckend"

# Step 3: Activate virtual environment
.\venv\Scripts\Activate.ps1

# Step 4: Check everything is working
python manage.py check

# Step 5: Apply any pending migrations
python manage.py migrate

# Step 6: Run the server
python manage.py runserver
```

**Result:** Server will be running at `http://127.0.0.1:8000/`

---

## Part 6: Multiple Terminals

### **Open Multiple Terminals**
1. Click the `+` icon in the terminal panel
2. Or press `Ctrl + Shift + `` (backtick)

### **Switch Between Terminals**
- Click on terminal name at the bottom
- Or use dropdown menu

### **Example Setup:**
- **Terminal 1:** Run Django server
- **Terminal 2:** Run other commands while server is running

---

## Part 7: Troubleshooting

### **Terminal Won't Open**
- Try menu: `View → Terminal`
- Or try keyboard shortcut: `Ctrl + Shift + P` then type "Toggle Integrated Terminal"

### **Command Not Found**
- Make sure you're in correct directory: `Get-Location`
- Use full path: `& "venv\Scripts\python.exe" ...`

### **Server Won't Start**
```powershell
# Check system
& "venv\Scripts\python.exe" manage.py check

# Clear Python cache
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse
```

### **Permission Denied**
If you get permission error, run as Administrator:
1. Close VS Code
2. Right-click VS Code
3. Select "Run as administrator"
4. Open project again

### **Port 8000 Already in Use**
Run on different port:
```powershell
& "venv\Scripts\python.exe" manage.py runserver 8001
```

---

## Part 8: Environment Variables

### **Check Virtual Environment is Active**
Look for `(venv)` at the start of terminal line:
```
(venv) PS C:\Users\Srishti\Desktop\hireFlow\bckend>
```

### **Deactivate Virtual Environment**
```powershell
deactivate
```

### **Reactivate Virtual Environment**
```powershell
.\venv\Scripts\Activate.ps1
```

---

## Part 9: Useful Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open/Close Terminal | `Ctrl + `` |
| New Terminal | `Ctrl + Shift + `` |
| Clear Terminal | `Ctrl + L` |
| Stop Running Command | `Ctrl + C` |
| Scroll Up | `Shift + Page Up` |
| Scroll Down | `Shift + Page Down` |
| Select All | `Ctrl + A` |
| Copy | `Ctrl + C` |
| Paste | `Ctrl + V` |

---

## Part 10: Running Python Scripts

### **Run Any Python Script**
```powershell
& "venv\Scripts\python.exe" script_name.py
```

### **Run Python Code Directly**
```powershell
& "venv\Scripts\python.exe" -c "print('Hello World')"
```

### **Run Django Management Command**
```powershell
& "venv\Scripts\python.exe" manage.py command_name [options]
```

---

## Quick Reference Commands

```powershell
# Navigate to project
Set-Location "C:\Users\Srishti\Desktop\hireFlow\bckend"

# Start server
& "venv\Scripts\python.exe" manage.py runserver

# Stop server
# Press: Ctrl + C

# Create app
& "venv\Scripts\python.exe" manage.py startapp myapp

# Make migrations
& "venv\Scripts\python.exe" manage.py makemigrations

# Apply migrations
& "venv\Scripts\python.exe" manage.py migrate

# Create admin user
& "venv\Scripts\python.exe" manage.py createsuperuser

# Django shell
& "venv\Scripts\python.exe" manage.py shell

# Check system
& "venv\Scripts\python.exe" manage.py check

# Collect static
& "venv\Scripts\python.exe" manage.py collectstatic

# List packages
& "venv\Scripts\python.exe" -m pip list

# Install package
& "venv\Scripts\python.exe" -m pip install package_name

# Update package
& "venv\Scripts\python.exe" -m pip install --upgrade package_name
```

---

## Notes

✓ Always navigate to `bckend` folder first
✓ Use full path if having issues: `& "venv\Scripts\python.exe" ...`
✓ Server runs indefinitely - you can open new terminals to run other commands
✓ Virtual environment keeps dependencies isolated
✓ Keep terminal window visible to see server logs

---

**Project Location:** `C:\Users\Srishti\Desktop\hireFlow\bckend`
**Server URL:** `http://127.0.0.1:8000/`
**Virtual Environment:** `venv/`
**Django Version:** 6.0.7
**Python Version:** 3.13.5
