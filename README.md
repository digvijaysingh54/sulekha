# ✨ Sulekha Singh - A Beautiful Soul Tribute Website

A modern, elegant, and responsive personal tribute website celebrating the life, journey, values, and beautiful heart of Sulekha Singh.

## 🌟 Features

- **Responsive Design**: Works perfectly on mobile, tablet, and desktop
- **Modern Aesthetics**: Soft, warm color palette with smooth animations
- **Multiple Sections**:
  - Homepage with hero section
  - Career Journey timeline
  - Hobbies & Interests gallery
  - Family & Responsibilities story
  - Personal Tribute section
  - Contact form
- **Smooth Animations**: Fade-in effects, scroll animations, and interactive elements
- **No External Dependencies**: Runs entirely offline with local assets
- **Easy to Customize**: Simple HTML/CSS structure for adding photos and personalizing content

## 📁 Project Structure

```
sulekha/
├── index.html              # Homepage
├── career.html             # Career journey timeline
├── hobbies.html            # Hobbies & interests
├── family.html             # Family & responsibilities
├── tribute.html            # Personal tribute section
├── contact.html            # Contact form
├── css/
│   └── style.css          # Main stylesheet with all designs
├── js/
│   └── script.js          # Interactive features & animations
├── images/                # Folder for uploading photos
│   ├── sulekha-hero.jpg           # Hero image (250x250)
│   ├── sulekha-professional.jpg   # Career page image
│   ├── sulekha-travel.jpg         # Travel/hobbies image
│   ├── sulekha-family.jpg         # Family page image
│   ├── sulekha-portrait.jpg       # Tribute page image
│   ├── sulekha-temple.jpg         # Temple visit image
│   ├── sulekha-beach.jpg          # Beach image
│   ├── sulekha-hills.jpg          # Hill station image
│   ├── sulekha-candid.jpg         # Candid photo
│   └── sulekha-smile.jpg          # Portrait with smile
└── README.md              # This file

```

## 🚀 Quick Start Guide

### Step 1: Download the Project
Clone or download this project to your local machine.

### Step 2: Add Your Photos
Place photos of Sulekha in the `images/` folder with the following names:
- `sulekha-hero.jpg` - Main hero image (display size: 250×250px)
- `sulekha-professional.jpg` - Career/professional photo
- `sulekha-travel.jpg` - Travel/candid photo
- `sulekha-family.jpg` - Family-related photo
- `sulekha-portrait.jpg` - Close-up portrait for tribute section
- `sulekha-temple.jpg` - Temple visit photo (or nature/spiritual image)
- `sulekha-beach.jpg` - Beach photo
- `sulekha-hills.jpg` - Hill station photo
- `sulekha-candid.jpg` - Candid moment
- `sulekha-smile.jpg` - Smiling portrait

**Note**: Photos are optional! The website includes placeholder images for missing photos, so you can start viewing immediately.

### Step 3: Open the Project
1. Open the project folder in VS Code or your favorite editor
2. Right-click on `index.html` and select "Open with Live Server" OR
3. Use the terminal method below

### Step 4: Run Locally

#### Option A: Using Python (Recommended for Windows/Mac/Linux)
```bash
cd path/to/sulekha
python -m http.server 8000
```
Then open your browser and go to: `http://localhost:8000`

#### Option B: Using Node.js (npx serve)
```bash
cd path/to/sulekha
npx serve
```
The terminal will show the local URL (usually `http://localhost:3000`)

#### Option C: Using Live Server Extension (VS Code)
1. Install "Live Server" extension by Ritwick Dey
2. Right-click on `index.html`
3. Select "Open with Live Server"
4. Browser opens automatically at `http://127.0.0.1:5500`

#### Option D: Direct Browser Open (Simplest)
Simply double-click `index.html` to open in your default browser. Note: Some features may be limited.

## 📝 Customization Guide

### Change Text Content
Edit the HTML files directly:
- **Homepage**: `index.html`
- **Career Timeline**: `career.html`
- **Hobbies**: `hobbies.html`
- **Family**: `family.html`
- **Tribute**: `tribute.html`
- **Contact**: `contact.html`

### Change Colors
Edit `css/style.css` and modify the CSS variables:
```css
:root {
  --primary-color: #e8f4f8;     /* Light blue background */
  --accent-pink: #f0d9e8;       /* Pastel pink */
  --accent-blue: #a8d5f7;       /* Light blue accents */
  --dark-blue: #2c5aa0;         /* Dark blue text/headings */
  --earth-brown: #8b7355;       /* Brown accents */
}
```

### Change Fonts
Modify the font-family in `css/style.css`:
```css
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
```

### Add More Sections
Copy an existing section in any HTML file and modify the content. Follow the existing structure for consistency.

## 🌐 Deployment Guide

### Deploy to GitHub Pages (Free)

1. **Create a GitHub account** (if you don't have one): https://github.com

2. **Create a new repository**:
   - Go to https://github.com/new
   - Name it: `sulekha-tribute` (or any name)
   - Choose "Public"
   - Click "Create repository"

3. **Upload files**:
   - Click "Add file" → "Upload files"
   - Upload all files (including folders)
   - Commit changes

4. **Enable GitHub Pages**:
   - Go to repository Settings
   - Scroll to "Pages" section
   - Select "main" branch as source
   - Save

5. **Access your site**:
   Your site will be live at: `https://yourusername.github.io/sulekha-tribute`

### Deploy to Netlify (Free & Easy)

1. **Prepare your files**: Ensure all files are in one folder locally

2. **Go to Netlify**: https://www.netlify.com

3. **Sign up**: Click "Sign up" and choose GitHub or email

4. **Deploy**:
   - Drag and drop your project folder into Netlify
   - Or connect your GitHub repository
   - Your site is instantly live!

5. **Access your site**: 
   Netlify provides a URL like: `https://your-site-name.netlify.app`

### Deploy to Vercel (Free)

1. **Go to Vercel**: https://vercel.com

2. **Sign up**: Connect with GitHub or email

3. **Deploy**:
   - Click "New Project"
   - Upload your project folder
   - Vercel automatically deploys

4. **Access your site**: 
   Your site gets a custom URL from Vercel

## 📸 Photo Recommendations

### Ideal Photo Specifications:
- **Format**: JPG or PNG
- **Size**: 1200×800px or larger (they'll be resized responsively)
- **Quality**: High quality, well-lit photos
- **Hero Image**: Square or slightly wider (250×250px display)
- **Full-page Images**: 1200×600px or similar

### Photo Tips:
- Use high-quality, well-lit photos
- Ensure faces are clearly visible
- Include variety: professional, casual, travel, family moments
- Use landscape orientation for gallery photos

## 🎨 Design Features

### Color Palette
- **Sky Blue**: Calm, peaceful, spiritual
- **Pastel Pink**: Warm, caring, loving
- **Earthy Brown**: Grounded, strong, natural
- **Dark Blue**: Professional, trustworthy

### Typography
- **Headings**: Bold, clear, readable
- **Body Text**: Clean, comfortable reading
- **Accents**: Italics for quotes and inspiration

### Animations
- Fade-in effects on page load
- Smooth hover transitions
- Scroll-triggered animations
- Parallax effects on hero section

## 🔧 Troubleshooting

### Photos Not Showing
- Check file names match exactly (case-sensitive on Mac/Linux)
- Ensure files are in the `images/` folder
- Supported formats: JPG, PNG, GIF, WebP

### Styling Looks Off
- Clear browser cache (Ctrl+Shift+Delete on Windows)
- Try a different browser
- Check that `css/style.css` is in the correct path

### Links Not Working
- Ensure HTML files are in the root folder
- Check file names in link references
- Verify case sensitivity (index.html not Index.html)

### Form Not Working (Local Testing)
- On local browsers, the form shows success message but doesn't send emails
- For email functionality, use Netlify Forms or a backend service

## 📱 Responsive Design

The website is fully responsive:
- **Desktop** (1200px+): Full layout with all features
- **Tablet** (768px-1199px): Optimized tablet view
- **Mobile** (320px-767px): Mobile-first design with touch-friendly elements

## ✨ Special Features

### Smooth Navigation
- Fixed navigation bar with scroll effects
- Mobile hamburger menu
- Smooth scroll animations

### Interactive Elements
- Hover effects on cards and images
- Progress bar showing scroll position
- Auto-highlighting navigation based on page position
- Contact form with validation

### Accessibility
- Semantic HTML structure
- Alt text for all images
- Readable color contrast
- Keyboard navigation support

## 📞 Support & Customization

For help customizing this website:
1. Check the Customization Guide section above
2. Modify CSS variables for colors
3. Edit HTML content directly
4. Add new sections by copying existing ones

## 📄 License

This tribute website is created with love and care. Feel free to use, modify, and personalize it. Share the beauty and inspiration it brings.

---

## 🎁 Final Notes

This website is a celebration of Sulekha Singh's beautiful soul. Use it to:
- Share her story with loved ones
- Inspire others with her journey
- Keep memories alive
- Express appreciation and love

**Remember**: The most important element is the heart behind it. Your personal touches and genuine celebration make this website truly special.

---

**Created with ❤️ for a beautiful soul**  
*"A beautiful soul deserves a beautiful world."*

