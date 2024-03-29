package {{package}};

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.utils.BeanCopyUtils;
import lombok.RequiredArgsConstructor;
import org.springframework.transaction.annotation.Transactional;
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
        return {{beanName}}Mapper.selectVoPage(
            query.build(),
            buildQuery(query),
            {{beanClassName}}ListVO.class
        );
    }

    @Transactional(rollbackFor = Throwable.class)
    @Override
    public void add({{beanClassName}}DTO {{beanName}}Dto) {
        {{beanClassName}}DO {{beanName}} = copyNonNull({{beanName}}Dto, {{beanClassName}}DO.class);
        {{beanName}}.genCreateInfo();
        {{beanName}}Mapper.insert({{beanName}});
    }

    @Override
    public {{beanClassName}}VO get(String id) {
        return {{beanName}}Mapper.selectVoById(id, {{beanClassName}}VO.class);
    }

    @Transactional(rollbackFor = Throwable.class)
    @Override
    public void update({{beanClassName}}DTO {{beanName}}Dto) {
        {{beanClassName}}DO {{beanName}} = copyNonNull({{beanName}}Dto, {{beanClassName}}DO.class);
        {{beanName}}.genUpdateInfo();
        {{beanName}}Mapper.updateById({{beanName}});
    }

    @Transactional(rollbackFor = Throwable.class)
    @Override
    public void delete(String id) {
        {{beanName}}Mapper.deleteById(id);
    }

    private LambdaQueryWrapper<{{beanClassName}}DO> buildQuery({{beanClassName}}Query query) {
        return Wrappers.<{{beanClassName}}DO>lambdaQuery()
            .orderByDesc({{beanClassName}}DO::getCreateTime);
    }
}
