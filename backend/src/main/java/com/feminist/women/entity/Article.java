package com.feminist.women.entity;

import lombok.Data;
import java.time.LocalDateTime;

@Data
public class Article {
    private Long id;
    private String title;
    private String content;
    private String category;
    private String author;
    private String coverImage;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
