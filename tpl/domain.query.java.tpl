package {{ package }};

import com.microsun.common.core.domain.PageQuery;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 * @author: {{ author }}
 * @date: {{ datetime }}
 */
@EqualsAndHashCode(callSuper = true)
@Data
@ApiModel("{{beanDesc}}查询")
public class {{beanClassName}}Query extends PageQuery {

    // TODO fields

    /**
     * t
     */
    @ApiModelProperty("t")
    private String t;
}
