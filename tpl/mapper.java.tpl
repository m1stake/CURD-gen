package {{ package }};

import com.microsun.common.core.mapper.BaseMapperPlus;
{% include 'part.importClass.tpl' %}
/**
 * {{beanDesc}}
 * @author {{author}}
 * @date {{datetime}}
 */
public interface {{beanClassName}}Mapper
    extends BaseMapperPlus<{{beanClassName}}Mapper, {{beanClassName}}DO, {{beanClassName}}DO> {

}
