from odoo import  fields, models, api

class College_Data(models.Model):
    _name = 'faculty.update'
    _description = "Faculty Infromation"

    faculty_name = fields.Many2one('college.faculty')

    def faculty_wizard_action(self):
       	self.env['college.faculty'].browse(self._context.get("active_ids")).update({"faculty_name":self.faculty_name})


