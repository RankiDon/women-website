package com.feminist.women.service;

import com.feminist.women.entity.Article;
import com.feminist.women.mapper.ArticleMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ArticleService {

    @Autowired
    private ArticleMapper articleMapper;

    public List<Article> findAll(String category, int page, int size) {
        int offset = page * size;
        return articleMapper.findAll(category, offset, size);
    }

    public Article findById(Long id) {
        return articleMapper.findById(id);
    }

    public Article create(Article article) {
        articleMapper.insert(article);
        return article;
    }

    public Article update(Long id, Article article) {
        article.setId(id);
        articleMapper.update(article);
        return articleMapper.findById(id);
    }

    public void delete(Long id) {
        articleMapper.deleteById(id);
    }

    public long count(String category) {
        return articleMapper.count(category);
    }

    public List<Article> findRelated(String category, Long excludeId, int limit) {
        return articleMapper.findRelated(category, excludeId, limit);
    }
}
