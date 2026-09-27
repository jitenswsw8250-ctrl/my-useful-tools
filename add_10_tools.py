# add_10_tools.py
# Builder script to generate and integrate the 10 new PDF & Image tools into MY USEFUL TOOLS

NEW_TOOLS_DATA = [
    {
        "id": "pdf-merge",
        "name": "PDF Merge",
        "icon": "📑",
        "category": "pdf-images",
        "desc": "Combine multiple PDF documents into one file in custom page order.",
        "tags": ["PDF", "Merge", "Combine", "Join", "Docs"]
    },
    {
        "id": "pdf-split",
        "name": "PDF Split",
        "icon": "✂️",
        "category": "pdf-images",
        "desc": "Extract custom page ranges or split single pages from any PDF document.",
        "tags": ["PDF", "Split", "Extract", "Pages", "Separate"]
    },
    {
        "id": "pdf-to-images",
        "name": "PDF to Images",
        "icon": "🖼️",
        "category": "pdf-images",
        "desc": "Convert multi-page PDF documents into high-resolution JPG or PNG images.",
        "tags": ["PDF", "Images", "Convert", "JPG", "PNG"]
    },
    {
        "id": "images-to-pdf",
        "name": "Images to PDF",
        "icon": "📑",
        "category": "pdf-images",
        "desc": "Combine multiple JPG, PNG, and WebP images into a single clean PDF.",
        "tags": ["Images", "PDF", "Photos", "Album", "Combine"]
    },
    {
        "id": "image-compressor",
        "name": "Image Compressor",
        "icon": "🗜️",
        "category": "pdf-images",
        "desc": "Reduce image file size while keeping visual clarity 100% locally.",
        "tags": ["Image", "Compress", "Reduce", "Optimize", "Size"]
    },
    {
        "id": "image-resizer",
        "name": "Image Resizer",
        "icon": "📐",
        "category": "pdf-images",
        "desc": "Resize images to exact pixel dimensions or percentage scales.",
        "tags": ["Image", "Resize", "Scale", "Dimensions", "Pixels"]
    },
    {
        "id": "jpg-to-png",
        "name": "JPG to PNG Converter",
        "icon": "🔁",
        "category": "pdf-images",
        "desc": "Convert JPG and JPEG images to lossless high-clarity PNG format.",
        "tags": ["JPG", "PNG", "Convert", "Image", "Format"]
    },
    {
        "id": "png-to-jpg",
        "name": "PNG to JPG Converter",
        "icon": "🔄",
        "category": "pdf-images",
        "desc": "Transform PNG graphics into compressed JPGs with custom background color.",
        "tags": ["PNG", "JPG", "Convert", "Transparent", "Image"]
    },
    {
        "id": "image-cropper",
        "name": "Image Cropper",
        "icon": "✂️",
        "category": "pdf-images",
        "desc": "Crop photos and graphics with standard aspect ratio presets or custom box.",
        "tags": ["Image", "Crop", "Trim", "Square", "16:9"]
    },
    {
        "id": "image-to-webp",
        "name": "Image to WebP Converter",
        "icon": "⚡",
        "category": "pdf-images",
        "desc": "Convert JPG and PNG images to ultra-lightweight next-gen WebP format.",
        "tags": ["WebP", "Image", "Fast", "Next-Gen", "Convert"]
    }
]

print(f"Loaded {len(NEW_TOOLS_DATA)} tool definitions.")
