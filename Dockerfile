# Use a lightweight nginx image
FROM nginx:alpine

# Copy the app files into the nginx web root
COPY src /usr/share/nginx/html

# Expose port 80
EXPOSE 80
