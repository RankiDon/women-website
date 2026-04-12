package com.feminist.women.mapper;

import com.feminist.women.entity.Article;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface ArticleMapper {

    List<Article> findAll(@Param("category") String category, @Param("offset") int offset, @Param("limit") int limit);

    Article findById(@Param("id") Long id);

    int insert(Article article);

    int update(Article article);

    int deleteById(@Param("id") Long id);

    long count(@Param("category") String category);

    List<Article> findRelated(@Param("category") String category, @Param("excludeId") Long excludeId, @Param("limit") int limit);
}
