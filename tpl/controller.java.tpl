package {{package}};

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 *
 * @author {{ author }}
 * @date {{ datetime }}
 */
@RestController
@RequestMapping("{{reqMapping}}")
@Api(tags = "{{beanDesc}}")
@RequiredArgsConstructor
public class {{beanClassName}}Controller {

    private final {{beanClassName}}Service {{beanName}}Service;

    /**
     * 列表查询
     * @param query 查询参数
     */
    @ApiOperation("查询列表")
    @GetMapping
    public Page<{{beanClassName}}ListVO> query({{beanClassName}}Query query) {
        return {{beanName}}Service.query(query);
    }

    /**
     * 新增
     */
    @ApiOperation("新增")
    @PostMapping
    public void add(@RequestBody {{beanClassName}}DTO {{beanName}}Dto) {
       {{beanName}}Service.add({{beanName}}Dto);
    }

    /**
     * 查询详细信息
     */
    @ApiOperation("查询详细信息")
    @GetMapping("{id}")
    public {{beanClassName}}VO get(@PathVariable String id) {
        return {{beanName}}Service.get(id);
    }

    /**
     * 修改
     */
    @ApiOperation("修改")
    @PutMapping
    public void update(@RequestBody {{beanClassName}}DTO {{beanName}}Dto) {
        {{beanName}}Service.update({{beanName}}Dto);
    }

    /**
     * 删除
     */
    @ApiOperation("删除")
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        {{beanName}}Service.delete(id);
    }

}
