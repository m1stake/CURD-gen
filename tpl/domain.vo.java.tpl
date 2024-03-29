package {{ package }};

import com.domain.AbstractVO;
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
@ApiModel("{{ beanDesc }}vo")
@EqualsAndHashCode(callSuper = true)
public class {{ beanClassName }}VO extends AbstractVO {
{% include 'part.apiField.tpl' %}
}