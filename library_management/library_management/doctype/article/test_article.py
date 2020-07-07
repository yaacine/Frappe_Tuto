# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import frappe.defaults
import unittest

def create_articles():
    
    if frappe.flags.test_articles_created:
        return
    # delete all records before inserting
    frappe.db.delete('Article',{"author":"yacine"})
    frappe.db.commit()

    frappe.set_user("Administrator")
    doc = frappe.get_doc({
        "doctype": "Article",
        "article_name":"_Test Article 1",
        "author": "yacine",
        "isbn": "123455",
        "status": "Available",
        "publisher": "yacine edition",
        "language": "english",
        "image": "",
        "description": "Eiusmod aliquip cillum ipsum enim non est laboris ullamco velit anim irure proident. Cupidatat aliqua occaecat irure consequat ut duis enim veniam ut aliquip ipsum magna aliquip esse. Anim ea fugiat dolore ut adipisicing mollit sunt anim incididunt. Labore culpa amet consequat qui Lorem elit qui sunt. Irure culpa do pariatur eiusmod aliquip nisi enim reprehenderit sit officia laborum amet nulla. Deserunt velit commodo anim sunt exercitation."
    }).insert()

    doc = frappe.get_doc({
        "doctype": "Article",
        "article_name":"_Test Article 2",
        "author": "yacine",
        "isbn": "123455",
        "status": "Available",
        "publisher": "yacine edition",
        "language": "english",
        "image": "",
        "description": "In do deserunt eiusmod Lorem sunt eiusmod sint ipsum adipisicing ex. Laborum laborum consequat minim reprehenderit adipisicing qui consectetur aute duis elit. Proident eiusmod enim excepteur eu eiusmod cupidatat est Lorem reprehenderit ad. Laborum nostrud magna ullamco consequat aliquip sunt anim laborum mollit sint irure est amet."
    }).insert()
    doc = frappe.get_doc({
        "doctype": "Article",
        "article_name":"_Test Article 3",
        "author": "yacine",
        "isbn": "123455",
        "status": "Available",
        "publisher": "yacine edition",
        "language": "english",
        "image": "",
        "description": "Labore occaecat quis tempor dolor velit et. Irure pariatur exercitation incididunt mollit nulla officia ut veniam nisi. Ut ullamco culpa consectetur cupidatat non adipisicing excepteur reprehenderit nostrud Lorem fugiat occaecat ad. Fugiat deserunt nulla incididunt est proident do amet dolor culpa exercitation Lorem ex nisi."
        
    }).insert()

    frappe.flags.test_articles_created = True


class TestArticle(unittest.TestCase):
    def setUp(self):
        create_articles()
    
    def tearDown(self):
        frappe.set_user("Administrator")
    
    def test_allowed_public(self):
        frappe.set_user("hamid@gmail.com")
        doc = frappe.get_doc("Article", frappe.db.get_value("Article",
            {"article_name":"_Test Article 1"}))
        self.assertTrue(frappe.has_permission("Article", doc=doc))

    def test_articles_list(self):
        frappe.set_user("test1@example.com")
        res = frappe.get_list("Article",  fields=["article_name", "author"])
        self.assertEquals(len(res), 3)
        article_names = [r.article_name for r in res]
        self.assertTrue("_Test Article 1" in article_names)
        self.assertTrue("_Test Article 3" in article_names)
        self.assertFalse("_Test Article 4" in article_names)
    

   