package {{ package }};

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 *
 * @author {{ author }}
 * @date {{ datetime }}
 */
@Data
@ApiModel("{{ beanDesc }}dto")
public class {{ beanClassName }}DTO {
{% include 'part.apiField.tpl' %}
}