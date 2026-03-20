package com.pharma.login;

import org.springframework.stereotype.Service;

@Service
public class AuthService {
    public boolean authenticate(String username, String password) {
        if (username == null || password == null) return false;
        return "admin".equalsIgnoreCase(username.trim()) && "admin".equals(password.trim());
    }
}
