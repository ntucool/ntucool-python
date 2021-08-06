let properties = [];
$x('//*[@id="content"]/div/div[3]/pre/code')[0].textContent.split(/\n+/).forEach((element) => {
    element = element.trim();
    if (element.startsWith('{')) {
        if (properties.length === 0) {
            let property = {
                'docstrings': [],
            };
            properties.push(property);
        }
    } else if (element.startsWith('//')) {
        if (properties.length > 0) {
            properties[properties.length - 1]['docstrings'].push(element.slice(3));
        }
    } else if (element.startsWith('"')) {
        properties[properties.length - 1]['name'] = element.split('": ')[0].slice(1, element.length - 1);
        let property = {
            'docstrings': [],
        };
        properties.push(property);
    }
});
if (!('name' in properties[properties.length - 1])) {
    properties.pop();
}
console.log(properties);
let text = '';
properties.forEach(element => {
    let t = '';
    if (element['docstrings'].length > 0) {
        element['docstrings'].forEach(e => {
            t += `  /// ${e}\n`;
        });
    }
    let name = element['name'].replace(/-/g, '_').split('_').map((value, index) => {
        if (value === '') return value;
        let prefix;
        if (index == 0) {
            prefix = value[0].toLowerCase();
        } else {
            prefix = value[0].toUpperCase();
        }
        value = prefix + value.slice(1);
        return value;
    }).join('');
    t += `  Object? get ${name} => getattr(\'${element['name']}\');`;
    text += t + '\n';
});
console.log(text);
setTimeout(async () => {
    await navigator.clipboard.writeText(text);
}, 1000);
