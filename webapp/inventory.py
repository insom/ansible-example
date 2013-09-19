from flask import Blueprint, jsonify
from .models import Machine
from ansible.inventory import Inventory
from ansible.playbook import PlayBook
from ansible import callbacks

inventory = Blueprint('inventory', __name__)


@inventory.route('/run')
def run():
    machines = Machine.query.all()
    inventory = Inventory([machine.name for machine in machines])
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks()
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats)
    results = PlayBook(playbook='webapp/test.yml',
                       callbacks=playbook_cb,
                       runner_callbacks=runner_cb,
                       stats=stats,
                       inventory=inventory).run()
    return jsonify(results)
