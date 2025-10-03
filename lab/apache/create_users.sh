#!/bin/bash

echo "Creating Apache password file with proper password hashes..."

# Create the password file (this will overwrite existing file)
htpasswd -cb .htpasswd admin admin123
htpasswd -b .htpasswd alice admin123  
htpasswd -b .htpasswd bob admin123
htpasswd -b .htpasswd user1 user123
htpasswd -b .htpasswd user2 user123

echo "Password file created successfully!"
echo ""
echo "Users created:"
echo "- admin:admin123 (admin group)"
echo "- alice:admin123 (admin group)" 
echo "- bob:admin123 (admin group)"
echo "- user1:user123 (users group)"
echo "- user2:user123 (users group)"
echo ""
echo "Only users in the 'admin' group can access /admin endpoints"