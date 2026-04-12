package com.feminist.women.mapper;

import com.feminist.women.entity.Category;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface CategoryMapper {

    List<Category> findAll();

    Category findById(Long id);

    int insert(Category category);

    int deleteById(Long id);
}
