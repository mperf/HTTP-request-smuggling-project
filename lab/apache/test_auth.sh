#!/bin/bash

BASE_URL="http://localhost"

# Test /admin with no auth
echo "Test: /admin (no auth) should be 401 Unauthorized"
curl -s -o /dev/null -w "%{http_code}\n" "$BASE_URL/admin"

# Test /admin with admin credentials
echo "Test: /admin (admin:admin123) should be 200 OK"
curl -s -o /dev/null -w "%{http_code}\n" -u admin:admin123 "$BASE_URL/admin"

# Test /admin with non-admin credentials
echo "Test: /admin (user1:user123) should be 403 Forbidden"
curl -s -o /dev/null -w "%{http_code}\n" -u user1:user123 "$BASE_URL/admin"

# Test /public with no auth
echo "Test: /public (no auth) should be 200 OK"
curl -s -o /dev/null -w "%{http_code}\n" "$BASE_URL/public"
