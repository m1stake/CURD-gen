package {{ package }};

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
{% include 'part.importClass.tpl' %}
/**
 * {{beanDesc}}
 * @author {{author}}
 * @date {{datetime}}
 */
public interface {{beanClassName}}Mapper extends BaseMapper<{{beanClassName}}DO> {

}
