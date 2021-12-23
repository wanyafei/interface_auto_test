# interface_auto_test
接口自动化测试框架:python+requests+unittest+BeautifulReport

1.运行 api_create_pys下的makepy.py生成对应的用例脚本
2.excel规范
    ①所有数字以文本格式存储
    ②头信息必须包含Content-Type
    ③若入参为空，则填写{}，必须为json
    ④验证方式：code,响应码  key，响应内容某个键值  sql，去查数据库
    ⑤依赖方式：key，某个接口的响应键值  sql，查询数据库 【因智慧信贷系统几乎都是单接口，不涉及关联接口，该功能暂时未做】
    ⑥sheet名称为系统中大模块名称-必输，模块名称为系统中子模块的名称-必输，用例名称为子模块下的接口名称-必输，序号为数字顺延-必输
    ⑦在配置文件ini中，可以通过控制is_run来实现批量运行还是单个运行，"#"注释的是不运行的。
