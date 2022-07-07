package {{ package }};

import com.microsun.common.core.domain.AbstractVO;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 *
 * @author {{ author }}
 * @date {{ datetime }}
 */
@Data
@ApiModel("{{ beanDesc }}列表vo")
@EqualsAndHashCode(callSuper = true)
public class {{ beanClassName }}ListVO extends AbstractVO {
{% include 'part.apiField.tpl' %}
}