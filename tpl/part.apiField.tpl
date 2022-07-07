{% for field in fields %}
    /**
     * {{ field.comment }}
     */
    @ApiModelProperty("{{ field.comment }}"){% if field.dateFormat %}
    @DateTimeFormat(pattern = "{{field.dateFormat}}"){% endif %}
    private {{ field.type }} {{ field.name }};
{% endfor %}