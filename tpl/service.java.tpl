package {{ package }};

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 * @author: {{ author }}
 * @date: {{ datetime }}
 */
public interface {{beanClassName}}Service {

    /**
     * 查询列表
     */
    Page<{{beanClassName}}ListVO> query({{beanClassName}}Query query);

    /**
     * 新增
     */
    void add({{beanClassName}}DTO {{beanName}}Dto);

    /**
     * 修改
     */
    void update({{beanClassName}}DTO {{beanName}}Dto);

    /**
     * 获取详细信息
     */
    {{beanClassName}}VO get(String id);

    /**
     * 删除
     */
    void delete(String id);
}
