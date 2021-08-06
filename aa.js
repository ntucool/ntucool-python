let properties = [];
$x('//*[@id="content"]/div/div[1]/pre/code')[0].textContent.split(/\n+/).forEach((element) => {
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
    let t = `@property\ndef ${element['name'].replace(/-/g, '_')}(self):\n    `;
    if (element['docstrings'].length > 1) {
        t += '"""';
        element['docstrings'].forEach(e => {
            t += `\n    ${e}`;
        });
        t += '\n    ';
        t += '"""\n    ';
    } else if (element['docstrings'].length == 1) {
        t += '"""';
        t += `${element['docstrings'][0]}`;
        t += '"""\n    ';
    }
    t += `return self.getattr(\'${element['name']}\')`;
    // console.log(t);
    text += t + '\n';
});
console.log(text);
setTimeout(async () => {
    await navigator.clipboard.writeText(text);
}, 1000);
