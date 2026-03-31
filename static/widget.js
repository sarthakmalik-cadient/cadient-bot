(function() {
    const s = document.currentScript || Array.from(document.getElementsByTagName('script')).find(n => n.src.includes('widget.js'));
    const aid = s ? s.getAttribute('data-agent-id') : '';
    const aky = s ? s.getAttribute('data-api-key') : '';
    
    const d = document.createElement('details');
    d.style.cssText = 'position:fixed;bottom:20px;right:20px;z-index:999';
    d.innerHTML = `
        <summary style="width:50px;height:50px;background:#2563eb;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;list-style:none">💬</summary>
        <iframe src="/?agent_id=${aid}&api_key=${aky}" style="width:350px;height:500px;border:1px solid #ddd;position:absolute;bottom:60px;right:0;border-radius:10px;background:#fff;margin:0;display:block"></iframe>
    `;
    document.body.appendChild(d);
})();
