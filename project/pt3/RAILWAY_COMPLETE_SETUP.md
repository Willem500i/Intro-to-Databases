# Complete Railway Setup - Flask App + Database

This guide will help you set up BOTH your Flask website and MySQL database on Railway.

## Step 1: Push Your Code to GitHub (If Not Done)

1. **Go to your project folder**:
   ```bash
   cd "/Users/willem/Library/CloudStorage/GoogleDrive-wdn2012@nyu.edu/My Drive/F2025/Intro to Databases/project/pt3"
   ```

2. **Initialize git and push** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Ready for Railway deployment"
   
   # Create a new repository on GitHub.com, then:
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Create Your Flask Web Service

1. **Go to Railway**: https://railway.app
2. **Sign up/Login** with GitHub
3. **Click "New Project"** (top right)
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository** from the list
6. **Railway will auto-detect Flask** and start deploying

**This creates your Flask web service!** ✅

---

## Step 3: Add MySQL Database

1. **In your Railway project**, you should see your Flask service
2. **Click "+ New"** button (top right, or in the project view)
3. **Select "Database"**
4. **Choose "Add MySQL"**
5. **Railway will create a MySQL database** automatically

**This creates your MySQL database!** ✅

Now you have TWO services:
- Your Flask web service (the website)
- Your MySQL database service

---

## Step 4: Connect Database to Your Flask App

1. **Click on your Flask web service** (not the database, the one with your app name)
2. **Click the "Variables" tab** (in the service settings)
3. **Click "New Variable"**
4. **Add the database connection**:
   - **Name**: `MYSQL_URL`
   - **Value**: Click the dropdown/icon next to the input
   - **Select**: `${{ MySQL.MYSQL_URL }}` (this references your MySQL service)
   - **Click "Add"**

5. **Add SECRET_KEY**:
   - **Click "New Variable"** again
   - **Name**: `SECRET_KEY`
   - **Value**: Generate one by running this locally:
     ```python
     python3 -c "import secrets; print(secrets.token_hex(32))"
     ```
     Or use any long random string (at least 32 characters)
   - **Click "Add"**

---

## Step 5: Initialize Your Database (Add Tables and Data)

Your database is empty - you need to add your tables!

### Option A: Using Railway's Query Tab (Easiest) ⭐

1. **Click on your MySQL database service** (not the web service)
2. **Click the "Query" tab** (or "Data" tab)
3. **Open your `schema.sql` file** locally
4. **Copy ALL the SQL** from `schema.sql`
5. **Paste it into Railway's Query tab**
6. **Click "Run"** or press Execute (usually a play button ▶️)
7. **Wait for success message**
8. **Now open your `sample_data.sql` file**
9. **Copy ALL the SQL** from `sample_data.sql`
10. **Paste it into Railway's Query tab**
11. **Click "Run"** again

✅ Your database now has tables and sample data!

### Option B: Using MySQL Command Line

1. **In Railway, go to your MySQL database service**
2. **Click "Connect" tab** or "Variables" tab
3. **Find the connection command**, something like:
   ```
   mysql -h yamabiko.proxy.rlwy.net -u root -p --port 32972 --protocol=TCP railway
   ```
4. **Run this in your terminal** (it will ask for password - get it from Railway's database variables)
5. **Then run**:
   ```sql
   SOURCE /full/path/to/your/schema.sql;
   SOURCE /full/path/to/your/sample_data.sql;
   ```

---

## Step 6: Deploy and Test

1. **Railway should auto-deploy** when you push to GitHub
2. **Or manually deploy**: Go to your Flask service → "Deployments" → "Redeploy"
3. **Check the logs**: Click "View Logs" to see if there are any errors
4. **Get your app URL**: 
   - Go to your Flask service
   - Click "Settings" tab
   - Find "Domains" section
   - Your app URL will be something like: `https://your-app-name.up.railway.app`
   - **Or** click "Generate Domain" to get a custom URL

5. **Visit your URL** in a browser! 🎉

---

## Visual Guide - What You Should See

In Railway, your project should look like this:

```
📁 Your Project Name
  ├── 🌐 Flask Web Service (your-app-name)
  │   ├── Variables tab → MYSQL_URL, SECRET_KEY
  │   ├── Deployments tab → View logs
  │   └── Settings tab → Your app URL
  │
  └── 🗄️ MySQL Database
      ├── Variables tab → Connection info
      └── Query tab → Run your SQL files here
```

---

## Troubleshooting

### "I can't find my Flask service"
- Make sure you deployed from GitHub
- Check that Railway detected Flask (should show Python/Flask in the service)

### "Database connection error"
- Check that `MYSQL_URL` variable is set correctly
- Make sure you used `${{ MySQL.MYSQL_URL }}` (with the `${{ }}` syntax)
- Check logs in your Flask service for connection errors

### "Tables don't exist"
- You haven't run `schema.sql` yet
- Go to MySQL service → Query tab → Run your schema.sql

### "How do I see my website URL?"
- Go to Flask service → Settings tab → Domains section
- Or check the "Deployments" tab for the URL

### "The app won't start"
- Check logs in Flask service → Deployments → View Logs
- Make sure all environment variables are set
- Verify `requirements.txt` has all dependencies

---

## Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Created Railway project from GitHub
- [ ] Added MySQL database service
- [ ] Set `MYSQL_URL` variable in Flask service
- [ ] Set `SECRET_KEY` variable in Flask service
- [ ] Ran `schema.sql` in database Query tab
- [ ] Ran `sample_data.sql` in database Query tab
- [ ] Checked app logs (no errors)
- [ ] Got app URL from Settings
- [ ] Tested the website in browser

---

## Your Live Website URL

After setup, your website will be accessible at:
```
https://your-app-name.up.railway.app
```

**Share this URL with anyone!** It's your live, working application.

---

## Need Help?

- Railway Dashboard: https://railway.app/dashboard
- Railway Docs: https://docs.railway.app
- Check logs: Flask service → Deployments → View Logs

