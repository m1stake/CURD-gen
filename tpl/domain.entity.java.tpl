package {{ package }};

import com.baomidou.mybatisplus.annotation.TableName;
import com.microsun.common.core.domain.AbstractEntity;
import lombok.Data;
import lombok.EqualsAndHashCode;
{% include 'part.importClass.tpl' %}
/**
 * {{ beanDesc }}
 *
 * @author {{ author }}
 * @date {{ datetime }}
 */
@EqualsAndHashCode(callSuper = true)
@Data
@TableName("{{ tableName }}")
public class {{ beanClassName }}DO extends AbstractEntity {
  {% for field in fields %}
    /**
     * {{ field.comment }}
     */
    private {{ field.type }} {{ field.name }};
  {% endfor %}
}