# AIAP Lecture Structure Guide

## 📚 **Overview**

This guide explains the standardized structure for AI Assisted Programming lectures, ensuring consistency, maintainability, and optimal Reveal.js performance.

## 🏗️ **Architecture**

### **Shared Theme System**
- **`theme/aiap-custom.css`** - Contains ALL common styles
- **Individual HTML files** - Clean, focused on content only
- **Template file** - `lecture-template.html` for new lectures

### **File Organization**
```
lectures/
├── lecture1-module-introduction.html       ✅ Clean
├── lecture2-ai-assisted-programming-intro.html ✅ Clean
├── lecture-template.html                   📋 Template
└── [future lectures...]

theme/
└── aiap-custom.css                         🎨 Shared styles
```

## 🎯 **Best Practices Applied**

### **Reveal.js Configuration (Consistent across all lectures)**
```javascript
Reveal.initialize({
    // Optimal responsive layout
    width: 960,
    height: 700,
    margin: 0.04,
    minScale: 0.2,
    maxScale: 2.0,
    
    // Educational content optimizations
    transition: 'convex',
    backgroundTransition: 'fade',
    autoAnimate: true,
    
    // Enhanced accessibility
    hash: true,
    controls: true,
    fragments: true,
});
```

### **CSS Organization**
- **Custom Properties** for consistent theming
- **Responsive design** with `clamp()` functions
- **Reveal.js layout helpers** (`.r-hstack`, `.r-vstack`, `.r-stretch`)
- **Mobile-first** responsive patterns

### **Slide Structure Patterns**

#### **Title Slide**
```html
<section data-state="title" class="title-slide">
    <div class="r-vstack">
        <h1>Lecture Title</h1>
        <div class="subtitle">Subtitle</div>
        <div class="section-divider"></div>
        <div class="instructor-info">Course info</div>
    </div>
</section>
```

#### **Two-Column Layout**
```html
<section>
    <h2>Section Title</h2>
    <div class="r-hstack">
        <div>Left content</div>
        <div>Right content</div>
    </div>
</section>
```

#### **Professional Quote**
```html
<div class="professional-quote">
    Important quote or callout text
</div>
```

## 🚀 **Creating New Lectures**

### **Step 1: Copy Template**
```bash
cp lecture-template.html lectures/lectureX-topic-name.html
```

### **Step 2: Customize Content**
1. Update title and meta information
2. Replace placeholder content
3. Add lecture-specific slides
4. Update learning outcomes

### **Step 3: NO Custom Styles**
- ❌ **Don't add** `<style>` blocks
- ❌ **Don't duplicate** existing CSS
- ✅ **Use existing** classes from `aiap-custom.css`
- ✅ **Follow** established patterns

### **Step 4: Test Responsiveness**
- Check desktop (1920x1080)
- Check tablet (768x1024)
- Check mobile (360x640)

## 📱 **Responsive Design Features**

### **Automatic Adaptations**
- Text scales with `clamp()` functions
- Images adapt with `min-width` constraints  
- Grids become single-column on mobile
- Navigation remains accessible

### **Layout Helpers Available**
- `.r-vstack` - Vertical stacking
- `.r-hstack` - Horizontal stacking (responsive)
- `.r-stretch` - Fill available space
- `.r-fit-text` - Auto-size text
- `.grid-2-col` - Two-column grid

## 🎨 **Styling Components**

### **Available Classes**
- `.professional-quote` - Highlighted quote blocks
- `.section-divider` - Visual section breaks
- `.stat-card` - Statistics display
- `.assessment-card` - Assessment information
- `.comparison-table` - Responsive tables

### **Color Variables**
```css
--primary-color: #2563eb
--secondary-color: #4f46e5
--accent-color: #f9fafb
--text-color: #374151
--success-color: #16a34a
--warning-color: #dc2626
```

## 📊 **Current Implementation Status**

### ✅ **Completed**
- [x] Duplicate styles removed from individual files
- [x] Shared theme system established
- [x] Responsive design optimized
- [x] Reveal.js best practices applied
- [x] Template created for future lectures
- [x] Configuration standardized

### 🔧 **For Future Lectures**
1. Copy `lecture-template.html`
2. Follow established patterns
3. Use existing CSS classes
4. Test across devices
5. Maintain consistency

## 🏆 **Benefits Achieved**

- **Maintainability**: Single source of truth for styles
- **Consistency**: All lectures look and behave the same
- **Performance**: Reduced CSS duplication
- **Responsiveness**: Optimized for all devices
- **Standards**: Following Reveal.js best practices
- **Scalability**: Easy to add new lectures

---

**For questions or improvements, refer to this guide and the `aiap-custom.css` file for available styling options.**