# Example 1: Safe file upload processing
def handle_file_upload(uploaded_file, allowed_types=None, max_size=5*1024*1024):
    if allowed_types is None:
        allowed_types = ['image/jpeg', 'image/png', 'application/pdf']
    
    try:
        # Check file size
        if uploaded_file.size > max_size:
            raise FileTooLargeError(
                f"File size {uploaded_file.size} exceeds limit {max_size}"
            )
        
        # Check file type
        if uploaded_file.content_type not in allowed_types:
            raise InvalidFileTypeError(
                f"File type {uploaded_file.content_type} not allowed"
            )
        
        # Generate safe filename
        original_name = uploaded_file.name
        safe_name = os.path.basename(original_name)  # Remove path information
        safe_name = re.sub(r'[^\w\.-]', '_', safe_name)  # Sanitize filename
        
        # Save file
        with open(os.path.join(UPLOAD_DIR, safe_name), 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        # Return file information
        return {
            'original_name': original_name,
            'saved_name': safe_name,
            'size': uploaded_file.size,
            'content_type': uploaded_file.content_type
        }
        
    except IOError as e:
        logger.error("Failed to save uploaded file: %s", e)
        raise FileProcessingError("Failed to process uploaded file") from e
        
    except Exception as e:
        logger.error("Unexpected error during file upload: %s", e)
        raise FileProcessingError("File upload failed") from e

# Example 2: Image processing with error handling
def process_profile_image(image_path):
    try:
        with Image.open(image_path) as img:
            # Validate image
            if img.format not in ('JPEG', 'PNG'):
                raise InvalidImageError(
                    f"Unsupported image format: {img.format}"
                )
            
            # Create thumbnail
            img.thumbnail((300, 300))
            
            # Generate thumbnail path
            base, ext = os.path.splitext(image_path)
            thumb_path = f"{base}_thumb{ext}"
            
            # Save thumbnail
            img.save(thumb_path, img.format)
            
            return thumb_path
            
    except Image.DecompressionBombError as e:
        raise InvalidImageError("Image is too large to process") from e
        
    except IOError as e:
        raise InvalidImageError("Failed to process image") from e