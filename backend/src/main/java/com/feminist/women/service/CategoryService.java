package com.feminist.women.service;

import com.feminist.women.entity.Category;
import com.feminist.women.mapper.CategoryMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CategoryService {

    @Autowired
    private CategoryMapper categoryMapper;

    public List<Category> findAll() {
        return categoryMapper.findAll();
    }

    public Category findById(Long id) {
        return categoryMapper.findById(id);
    }

    public Category create(Category category) {
        categoryMapper.insert(category);
        return category;
    }

    public void delete(Long id) {
        categoryMapper.deleteById(id);
    }
}
