let method_details = document.querySelectorAll("#Services > div");
let text = '';
method_details.forEach(method_detail => {
    let a = method_detail.querySelector(':scope > h2 > a');
    let title = a.textContent.trim();
    let function_name = title.toLowerCase().replace(/-/g, '_').replace(/\.|\(|\)/g, '').split(/[\s|\/]+/).join('_');
    let href = a.href;

    let endpoints = [];
    let h3 = method_detail.querySelectorAll(':scope > h3');
    h3.forEach(element => {
        endpoints.push(element.textContent.trim());
    });
    let description = [];
    let p = method_detail.querySelectorAll(':scope > p');
    p.forEach(element => {
        description.push(element.textContent.trim());
    });
    let returns = [];
    let found = false;
    method_detail.childNodes.forEach(element => {
        if (element.nodeType == Node.TEXT_NODE && element.textContent.trim().startsWith('Returns')) {
            found = true;
        }
        if (found === true) {
            returns.push(element.textContent.trim());
        }
    });
    returns = returns.join(' ').trim();
    if (returns.startsWith('Returns ')) {
        returns = returns.slice('Returns '.length).trim();
    }
    let t = '';
    t += 'def ';
    t += function_name;
    t += '():\n    """\n    ';
    t += title;
    t += '\n\n    ';
    endpoints.forEach(element => {
        t += '`';
        t += element;
        t += '`\n\n    ';
    });
    description.forEach(element => {
        t += element;
        t += '\n\n    ';
    });
    t += href;
    if (returns !== '') {
        t += '\n\n    Returns:\n        ';
        t += returns;
    }
    t += '\n    """\n';
    text += t;
});

setTimeout(async () => {
    await navigator.clipboard.writeText(text);
}, 1000);