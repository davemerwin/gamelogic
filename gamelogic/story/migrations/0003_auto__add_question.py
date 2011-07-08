# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Question'
        db.create_table('story_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('story_question_appears_on', self.gf('django.db.models.fields.related.ForeignKey')(related_name='story_question', to=orm['story.Story'])),
            ('story_question_answer_goes_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='story_destination', to=orm['story.Story'])),
        ))
        db.send_create_signal('story', ['Question'])

        # Removing M2M table for field child on 'Story'
        db.delete_table('story_story_child')

    def backwards(self, orm):
        
        # Deleting model 'Question'
        db.delete_table('story_question')

        # Adding M2M table for field child on 'Story'
        db.create_table('story_story_child', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_story', models.ForeignKey(orm['story.story'], null=False)),
            ('to_story', models.ForeignKey(orm['story.story'], null=False))
        ))
        db.create_unique('story_story_child', ['from_story_id', 'to_story_id'])

    models = {
        'story.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'story_question_answer_goes_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'story_destination'", 'to': "orm['story.Story']"}),
            'story_question_appears_on': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'story_question'", 'to': "orm['story.Story']"})
        },
        'story.story': {
            'Meta': {'ordering': "('key',)", 'object_name': 'Story'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'editorial_alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'editorial_beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'editorial_gold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'story_parent'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['story.Story']"}),
            'science_alpha': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'science_beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'science_gold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['story']
