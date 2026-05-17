# 🚀 QUICK START - Get Running in 3 Steps

## Step 1: Add Photos (Optional)
Drop Sulekha's photos into the `images/` folder. The website works with placeholder images if you skip this.

## Step 2: Open Terminal & Run Server
Choose ONE of these options:

### Option A: Python (Windows/Mac/Linux) ⭐ EASIEST
```bash
cd path/to/sulekha
python -m http.server 8000
```

### Option B: NPX Serve
```bash
npx serve
```

### Option C: Node HTTP Server
```bash
node -e "require('http').createServer((req,res)=>{const fs=require('fs');res.writeHead(200);res.end(fs.readFileSync('./index.html'))}).listen(8000)"
```

## Step 3: Visit Your Site
Open your browser and go to:
- **Python**: http://localhost:8000
- **NPX Serve**: http://localhost:3000
- **Manual**: Open `index.html` directly

---

## 📸 Photo Naming Guide

Name your photos exactly like this:
```
sulekha-hero.jpg              → Hero section image
sulekha-professional.jpg      → Career page
sulekha-travel.jpg            → Hobbies gallery
sulekha-family.jpg            → Family page
sulekha-portrait.jpg          → Tribute page
sulekha-temple.jpg            → Hobbies (temple)
sulekha-beach.jpg             → Hobbies (beach)
sulekha-hills.jpg             → Hobbies (hills)
sulekha-candid.jpg            → Family section
sulekha-smile.jpg             → Family section
```

---

## 🌐 Deploy Online (Choose One)

### GitHub Pages (Free, Easy)
1. Create repo at github.com/new
2. Upload all files
3. Settings → Pages → Select main branch
4. Share your link: `https://yourname.github.io/repo-name`

### Netlify (Free, Easiest)
1. Go to netlify.com
2. Drag & drop your folder
3. Done! Share the instant link

### Vercel (Free, Fast)
1. Go to vercel.com
2. "New Project" → Select folder
3. Auto-deployed! Share link

---

## ✨ That's It!

Your beautiful tribute website is ready to share with the world. 🎉

**Need help?** Check the full README.md for detailed instructions.
