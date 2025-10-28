# simple_gui

A modern, stylish text manipulation application built with tkinter in Python3. This app features a clean, responsive interface that allows you to manipulate text with ease.

## Features

- **Modern User Interface**: Clean, flat design with a professional color scheme
- **Responsive Layout**: Resizable window with minimum size constraints (500x400 to 600x500)
- **Text Manipulation**: Set custom text and reverse it instantly
- **Rich Color Options**: Choose from 15 different colors for your text:
  - Red, Blue, Green, Black, White
  - Purple, Orange, Pink, Teal, Navy
  - Coral, Indigo, Crimson, Gold, Silver
- **Interactive Buttons**: Hover effects and visual feedback on all buttons
- **Professional Typography**: Uses Helvetica font family with proper sizing

## UI Improvements

### What's New:
- ✨ **Modern Color Scheme**: Clean white background with vibrant button colors
- 📏 **Better Spacing**: Proper padding and margins throughout the interface
- 🎨 **Styled Buttons**: Flat design with blue (Set Text), purple (Set Color), and red (Reverse Text) buttons
- 🖱️ **Hover Effects**: Buttons change shade when you hover over them
- 📱 **Responsive Design**: Window can be resized while maintaining layout integrity
- 🎯 **Visual Hierarchy**: Clear section labels and organized layout
- 🔄 **Enhanced Reverse Button**: Full-width button with emoji for better UX

### Resolved Issues:
- ✅ Fixed gray background issues - now uses consistent white backgrounds
- ✅ Improved text display area with bordered frame
- ✅ Made window resizable with proper constraints
- ✅ Added proper grid configuration for responsive behavior

## Preview

The application now features a modern, clean interface with improved usability and aesthetics.

![Modern Simple Text GUI](https://user-images.githubusercontent.com/83800421/200504214-31a2d2e9-4210-4bc4-9820-34e4a056c62f.png)

## Installation

Requires Python 3 with tkinter:

```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On macOS (usually pre-installed)
# If needed: brew install python-tk

# On Windows (usually included with Python)
```

## Usage

Simply run the application:

```bash
python3 main.py
```

Then:
1. Type your text in the input field and click "Set Text"
2. Choose a color from the dropdown and click "Set Color"
3. Click "🔄 Reverse Text" to reverse your text

## Technical Details

- Built with Python 3.12+
- Uses tkinter and ttk for the GUI
- Implements grid-based responsive layout
- Custom button styling with hover effects
- Modern flat design principles
