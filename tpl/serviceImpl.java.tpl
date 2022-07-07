package {{package}};

import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.microsun.common.utils.BeanCopyUtils;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 *
 * @author {{ author }}
 * @date {{ datetime }}
 */
@RequiredArgsConstructor
@Service
public class {{beanClassName}}ServiceImpl implements {{beanClassName}}Service {

    private final {{beanClassName}}Mapper {{beanName}}Mapper;

    @Override
    public Page<{{beanClassName}}ListVO> query({{beanClassName}}Query query) {
        Page<{{beanClassName}}DO> p = {{beanName}}Mapper.selectPage(
            PageUtil.getPage(query),
            buildQuery(query));
        return PageUtil.mapPage(p, {{beanClassName}}ListVO.class);
    }

    @Override
    public void add({{beanClassName}}DTO {{beanName}}Dto) {
        {{beanClassName}}DO {{beanName}} = BeanCopyUtils.copyNonNull({{beanName}}Dto, {{beanClassName}}DO.class);
        {{beanName}}.genCreateInfo();
        {{beanName}}Mapper.insert({{beanName}});
    }

    @Override
    public {{beanClassName}}VO get(String id) {
        {{beanClassName}}DO {{beanName}} = {{beanName}}Mapper.selectById(id);
        return BeanCopyUtils.copyNonNull({{beanName}}, {{beanClassName}}VO.class);
    }

    @Override
    public void delete(String id) {
        {{beanName}}Mapper.deleteById(id);
    }

    @Override
    public void update({{beanClassName}}DTO {{beanName}}Dto) {
        {{beanClassName}}DO {{beanName}} = BeanCopyUtils.copyNonNull({{beanName}}Dto, {{beanClassName}}DO.class);
        {{beanName}}.genUpdateInfo();
        {{beanName}}Mapper.updateById({{beanName}});
    }

    private LambdaQueryWrapper<{{beanClassName}}DO> buildQuery({{beanClassName}}Query query) {
        LambdaQueryWrapper<{{beanClassName}}DO> wrapper = Wrappers.<{{beanClassName}}DO>lambdaQuery()
            .orderByDesc({{beanClassName}}DO::getCreateTime);
        return wrapper;
    }
}
