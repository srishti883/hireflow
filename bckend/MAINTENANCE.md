# Django Project Maintenance Guide

## Table of Contents
1. [Daily Maintenance](#daily-maintenance)
2. [Weekly Maintenance](#weekly-maintenance)
3. [Monthly Maintenance](#monthly-maintenance)
4. [Database Management](#database-management)
5. [Dependency Management](#dependency-management)
6. [Security Checks](#security-checks)
7. [Performance Optimization](#performance-optimization)
8. [Troubleshooting](#troubleshooting)
9. [Backup & Recovery](#backup--recovery)

---

## Daily Maintenance

### 1. Check Server Status
```powershell
# Verify server is running
# Access: http://127.0.0.1:8000/

# Monitor logs for errors
# Look for any 500 errors or warnings in terminal
```

### 2. Review Error Logs
- Check terminal output for any exceptions
- Monitor console for deprecation warnings
- Note any failed migrations or startup issues

### 3. Database Integrity
```powershell
# Run system checks
& "venv\Scripts\python.exe" manage.py check

# Fix any identified issues immediately
```

---

## Weekly Maintenance

### 1. Update Dependencies
```powershell
# Activate virtual environment
Set-Location "bckend"
& "venv\Scripts\python.exe" -m pip list --outdated

# Check for security updates
& "venv\Scripts\python.exe" -m pip install --upgrade pip
```

### 2. Run Migrations Check
```powershell
# Check for unapplied migrations
& "venv\Scripts\python.exe" manage.py showmigrations

# Apply any pending migrations
& "venv\Scripts\python.exe" manage.py migrate
```

### 3. Database Cleanup
```powershell
# Remove expired sessions
& "venv\Scripts\python.exe" manage.py clearsessions

# Clear old cache data (if using cache)
& "venv\Scripts\python.exe" manage.py clear_cache
```

### 4. Code Quality Check
```powershell
# Collect static files
& "venv\Scripts\python.exe" manage.py collectstatic --noinput

# Check for any Django warnings
& "venv\Scripts\python.exe" manage.py check --deploy
```

---

## Monthly Maintenance

### 1. Dependency Audit
```powershell
# Create requirements.txt
& "venv\Scripts\python.exe" -m pip freeze > requirements.txt

# Check for security vulnerabilities
& "venv\Scripts\python.exe" -m pip install safety
& "venv\Scripts\python.exe" -m safety check
```

### 2. Full System Check
```powershell
# Run comprehensive Django checks
& "venv\Scripts\python.exe" manage.py check --deploy

# Review settings for security issues
# Check DEBUG = False in production
# Verify SECRET_KEY configuration
# Confirm ALLOWED_HOSTS setup
```

### 3. Database Maintenance
```powershell
# Analyze database performance
# Create database backups (see Backup section)

# Optimize database if using PostgreSQL
# VACUUM ANALYZE; (run on PostgreSQL directly)
```

### 4. Log Review
- Archive old log files
- Analyze error patterns
- Document recurring issues
- Plan fixes for common problems

---

## Database Management

### Migrations

```powershell
# Create new migration
& "venv\Scripts\python.exe" manage.py makemigrations

# Apply migrations
& "venv\Scripts\python.exe" manage.py migrate

# Check migration history
& "venv\Scripts\python.exe" manage.py showmigrations

# Revert to previous migration
& "venv\Scripts\python.exe" manage.py migrate app_name 0001
```

### Database Operations

```powershell
# Create database superuser
& "venv\Scripts\python.exe" manage.py createsuperuser

# Reset database (CAUTION: deletes all data)
# Step 1: Delete db.sqlite3
# Step 2: Run migrations
& "venv\Scripts\python.exe" manage.py migrate

# Shell access for queries
& "venv\Scripts\python.exe" manage.py shell
```

---

## Dependency Management

### Installing Packages

```powershell
# Install specific package
& "venv\Scripts\python.exe" -m pip install package_name

# Install with version
& "venv\Scripts\python.exe" -m pip install package_name==1.0.0

# Install from requirements.txt
& "venv\Scripts\python.exe" -m pip install -r requirements.txt
```

### Updating Packages

```powershell
# Update specific package
& "venv\Scripts\python.exe" -m pip install --upgrade package_name

# Update all packages
& "venv\Scripts\python.exe" -m pip install --upgrade -r requirements.txt

# Freeze current environment
& "venv\Scripts\python.exe" -m pip freeze > requirements.txt
```

### Current Core Dependencies

- Django 6.0.7
- Django REST Framework 3.17.1
- psycopg2-binary 2.9.12 (PostgreSQL driver)

---

## Security Checks

### Django Security

```powershell
# Check security issues
& "venv\Scripts\python.exe" manage.py check --deploy

# Verify settings
# ☐ DEBUG = False (in production)
# ☐ SECRET_KEY is strong and secret
# ☐ ALLOWED_HOSTS configured
# ☐ CSRF middleware enabled
# ☐ SECURE_BROWSER_XSS_FILTER = True
# ☐ SECURE_CONTENT_SECURITY_POLICY set
```

### Dependency Security

```powershell
# Install safety
& "venv\Scripts\python.exe" -m pip install safety

# Check for vulnerabilities
& "venv\Scripts\python.exe" -m safety check
```

### Regular Security Tasks

- Update Django and dependencies monthly
- Monitor security advisories
- Review authentication mechanisms
- Audit database permissions
- Check API authentication

---

## Performance Optimization

### Database Optimization

```powershell
# Add database indexes
# In models.py:
# class Meta:
#     indexes = [
#         models.Index(fields=['field_name']),
#     ]

# Query optimization
# Use select_related() for ForeignKey
# Use prefetch_related() for reverse relations
# Use only() and defer() for specific fields
```

### Caching

```powershell
# Configure caching in settings.py
# Implement query result caching
# Use page-level caching where appropriate
```

### Static Files

```powershell
# Collect static files
& "venv\Scripts\python.exe" manage.py collectstatic --noinput

# Minify and compress for production
```

---

## Troubleshooting

### Common Issues

#### 1. Server Won't Start
```powershell
# Check Python installation
& "venv\Scripts\python.exe" --version

# Verify dependencies
& "venv\Scripts\python.exe" -m pip list

# Run system check
& "venv\Scripts\python.exe" manage.py check

# Clear Python cache
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse
```

#### 2. Database Errors
```powershell
# Check connection settings in settings.py
# Verify PostgreSQL is running (if using PostgreSQL)
# Test database connection
& "venv\Scripts\python.exe" manage.py dbshell

# Reset migrations if needed
# Delete migration files and db
# Recreate migrations
& "venv\Scripts\python.exe" manage.py makemigrations
& "venv\Scripts\python.exe" manage.py migrate
```

#### 3. Import Errors
```powershell
# Reinstall dependencies
& "venv\Scripts\python.exe" -m pip install -r requirements.txt

# Clear cached imports
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item
```

#### 4. Static Files Not Loading
```powershell
# Collect static files
& "venv\Scripts\python.exe" manage.py collectstatic --noinput --clear

# Verify STATIC_URL and STATIC_ROOT in settings
```

---

## Backup & Recovery

### Creating Backups

```powershell
# Backup database (SQLite)
Copy-Item -Path "db.sqlite3" -Destination "db.sqlite3.backup"

# Backup database (PostgreSQL)
# Use: pg_dump -U username -d database_name > backup.sql

# Backup project files
# ZIP the entire bckend folder
```

### Scheduled Backup Script

```powershell
# Create scheduled_backup.ps1
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupPath = "C:\Backups\django_backup_$timestamp"
New-Item -ItemType Directory -Path $backupPath
Copy-Item -Path "db.sqlite3" -Destination "$backupPath\"
Copy-Item -Path "." -Destination "$backupPath\project" -Recurse
```

### Restoring from Backup

```powershell
# Restore database (SQLite)
Copy-Item -Path "db.sqlite3.backup" -Destination "db.sqlite3" -Force

# Restore database (PostgreSQL)
# Use: psql -U username -d database_name < backup.sql
```

---

## Maintenance Checklist

### Daily ☐
- [ ] Server running and accessible
- [ ] Check error logs
- [ ] Run system checks

### Weekly ☐
- [ ] Check for outdated packages
- [ ] Apply pending migrations
- [ ] Clean up sessions
- [ ] Collect static files

### Monthly ☐
- [ ] Security audit
- [ ] Dependency updates
- [ ] Database optimization
- [ ] Create backup
- [ ] Review logs

### Quarterly ☐
- [ ] Full security review
- [ ] Performance analysis
- [ ] Documentation update
- [ ] Archive old logs

---

## Useful Commands Reference

```powershell
# Navigate to project
Set-Location "C:\Users\Srishti\Desktop\hireFlow\bckend"

# Activate virtual environment (if needed)
& "venv\Scripts\Activate.ps1"

# Run server
& "venv\Scripts\python.exe"http://127.0.0.1:8000/

# Make migrations
& "venv\Scripts\python.exe" manage.py makemigrations

# Apply migrations
& "venv\Scripts\python.exe" manage.py migrate

# Create superuser
& "venv\Scripts\python.exe" manage.py createsuperuser

# Django shell
& "venv\Scripts\python.exe" manage.py shell

# Collect static files
& "venv\Scripts\python.exe" manage.py collectstatic

# Check project
& "venv\Scripts\python.exe" manage.py check

# Show migrations status
& "venv\Scripts\python.exe" manage.py showmigrations

# List installed packages
& "venv\Scripts\python.exe" -m pip list

# Freeze requirements
& "venv\Scripts\python.exe" -m pip freeze > requirements.txt
```

---

## Notes

- Always backup before making major changes
- Test updates in development before production
- Keep Django and DRF updated for security patches
- Monitor performance metrics regularly
- Document any custom configurations
- Keep this guide updated as your project evolves

---

**Last Updated:** 2026-07-13
**Project Location:** `C:\Users\Srishti\Desktop\hireFlow\bckend`
**Server URL:** `http://127.0.0.1:8000/`
