package com.pharma.login;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AuthServiceTest {
    private final AuthService authService = new AuthService();

    @Test
    void testAuthenticateWithValidCredentials() {
        assertTrue(authService.authenticate("admin", "admin"), "Should authenticate with correct credentials");
    }

    @Test
    void testAuthenticateWithInvalidUsername() {
        assertFalse(authService.authenticate("user", "admin"), "Should not authenticate with invalid username");
    }

    @Test
    void testAuthenticateWithInvalidPassword() {
        assertFalse(authService.authenticate("admin", "wrong"), "Should not authenticate with invalid password");
    }

    @Test
    void testAuthenticateWithNullValues() {
        assertFalse(authService.authenticate(null, null), "Should not authenticate with null values");
    }

    @Test
    void testAuthenticateWithSpacesAndCase() {
        assertTrue(authService.authenticate(" Admin ", "admin "), "Should authenticate ignoring spaces and case");
    }
}
