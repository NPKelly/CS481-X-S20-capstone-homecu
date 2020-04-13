Vue.component('vtable',{
    delimiters: ['[[', ']]'],
    template: 
    `<table>
        <tr>
            <th>Credit Union</th>
            <th>Vendor</th>
            <th>CU Name</th>
            <th>State</th>
            <th>Server</th>
            <th>Odyssey Status</th>
            <th>Type</th>
        </tr>
        {% for instance in data %}
            <tr> 
                <td>{{instance.code}}</td>
                <td></td>
                <td class="clickable">{{instance.name}}</td>
                <td>{{instance.state}}</td>
            </tr>
        {% endfor %}
    </table>`
});

new Vue({el:'#root'});