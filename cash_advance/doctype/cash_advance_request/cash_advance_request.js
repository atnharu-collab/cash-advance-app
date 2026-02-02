frappe.ui.form.on('Cash Advance Request', {
	refresh: function(frm) {
		// Add Calculate button
		frm.add_custom_button(__('Calculate'), function() {
			calculate_totals(frm);
		}, __('Actions'));
		
		// Auto-calculate on load if liquidation items exist
		if (frm.doc.liquidation && frm.doc.liquidation.length > 0) {
			calculate_totals(frm);
		}
	},
	
	// Calculate Total Requested from Amount Requested in liquidation table
	total_requested: function(frm) {
		calculate_totals(frm);
	},
	
	// Recalculate when liquidation table changes
	liquidation: function(frm, cdt, cdn) {
		calculate_totals(frm);
	},
	
	calculate: function(frm) {
		calculate_totals(frm);
	}
});

// Function to calculate all totals
function calculate_totals(frm) {
	let total_requested = 0;
	let total_liquidated = 0;
	
	// Calculate Total Requested from Amount Requested in liquidation table
	if (frm.doc.liquidation && frm.doc.liquidation.length > 0) {
		frm.doc.liquidation.forEach(function(row) {
			if (row.amount_requested) {
				total_requested += parseFloat(row.amount_requested) || 0;
			}
			if (row.amount_liquidated) {
				total_liquidated += parseFloat(row.amount_liquidated) || 0;
			}
		});
	}
	
	// Set the calculated values
	frm.set_value('total_requested', total_requested);
	frm.set_value('total_liquidated', total_liquidated);
	frm.set_value('unliquidated', total_requested - total_liquidated);
	
	// Refresh the form to show updated values
	frm.refresh_field('total_requested');
	frm.refresh_field('total_liquidated');
	frm.refresh_field('unliquidated');
}

// Handle changes in Cash Advance Liquidation child table
frappe.ui.form.on('Cash Advance Liquidation', {
	amount_requested: function(frm, cdt, cdn) {
		calculate_totals(frm);
	},
	
	amount_liquidated: function(frm, cdt, cdn) {
		// When Amount Liquidated changes, recalculate totals
		calculate_totals(frm);
	},
	
	liquidation_remove: function(frm, cdt, cdn) {
		// Recalculate when a row is removed
		calculate_totals(frm);
	}
});
