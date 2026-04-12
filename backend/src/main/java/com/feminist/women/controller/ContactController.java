package com.feminist.women.controller;

import com.feminist.women.entity.ContactMessage;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/contact")
public class ContactController {

    @PostMapping
    public ResponseEntity<Map<String, Object>> submit(@RequestBody ContactMessage contact) {
        // Log the contact message (in production, this would send an email)
        System.out.println("Contact form submission:");
        System.out.println("  Name: " + contact.getName());
        System.out.println("  Email: " + contact.getEmail());
        System.out.println("  Subject: " + contact.getSubject());
        System.out.println("  Message: " + contact.getMessage());

        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("message", "Thank you for your message! We'll get back to you soon.");

        return ResponseEntity.ok(response);
    }
}
