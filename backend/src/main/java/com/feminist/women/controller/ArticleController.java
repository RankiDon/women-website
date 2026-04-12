package com.feminist.women.controller;

import com.feminist.women.entity.Article;
import com.feminist.women.service.ArticleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/articles")
@CrossOrigin(origins = "*")
public class ArticleController {

    @Autowired
    private ArticleService articleService;

    @GetMapping
    public ResponseEntity<Map<String, Object>> list(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            @RequestParam(required = false) String category) {

        List<Article> articles = articleService.findAll(category, page, size);
        long total = articleService.count(category);

        Map<String, Object> response = new HashMap<>();
        response.put("articles", articles);
        response.put("total", total);
        response.put("page", page);
        response.put("size", size);
        response.put("totalPages", (int) Math.ceil((double) total / size));

        return ResponseEntity.ok(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Article> getById(@PathVariable Long id) {
        Article article = articleService.findById(id);
        if (article == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(article);
    }

    @PostMapping
    public ResponseEntity<Article> create(@RequestBody Article article) {
        Article created = articleService.create(article);
        return ResponseEntity.ok(created);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Article> update(@PathVariable Long id, @RequestBody Article article) {
        Article existing = articleService.findById(id);
        if (existing == null) {
            return ResponseEntity.notFound().build();
        }
        Article updated = articleService.update(id, article);
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        Article existing = articleService.findById(id);
        if (existing == null) {
            return ResponseEntity.notFound().build();
        }
        articleService.delete(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{id}/related")
    public ResponseEntity<List<Article>> related(@PathVariable Long id) {
        Article article = articleService.findById(id);
        if (article == null) {
            return ResponseEntity.notFound().build();
        }
        List<Article> related = articleService.findRelated(article.getCategory(), id, 3);
        return ResponseEntity.ok(related);
    }
}
