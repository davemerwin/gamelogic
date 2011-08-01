# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Image'
        db.create_table('story_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('media', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('story', ['Image'])

        # Adding model 'Media'
        db.create_table('story_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('media', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('story', ['Media'])

        # Renaming column for 'Story.media' to match new field type.
        db.rename_column('story_story', 'media', 'media_id')
        # Changing field 'Story.media'
        db.alter_column('story_story', 'media_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story.Media'], null=True))

        # Adding index on 'Story', fields ['media']
        db.create_index('story_story', ['media_id'])

        # Renaming column for 'Story.image' to match new field type.
        db.rename_column('story_story', 'image', 'image_id')
        # Changing field 'Story.image'
        db.alter_column('story_story', 'image_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['story.Image'], null=True))

        # Adding index on 'Story', fields ['image']
        db.create_index('story_story', ['image_id'])

    def backwards(self, orm):
        
        # Removing index on 'Story', fields ['image']
        db.delete_index('story_story', ['image_id'])

        # Removing index on 'Story', fields ['media']
        db.delete_index('story_story', ['media_id'])

        # Deleting model 'Image'
        db.delete_table('story_image')

        # Deleting model 'Media'
        db.delete_table('story_media')

        # Renaming column for 'Story.media' to match new field type.
        db.rename_column('story_story', 'media_id', 'media')
        # Changing field 'Story.media'
        db.alter_column('story_story', 'media', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100))

        # Renaming column for 'Story.image' to match new field type.
        db.rename_column('story_story', 'image_id', 'image')
        # Changing field 'Story.image'
        db.alter_column('story_story', 'image', self.gf('django.db.models.fields.files.ImageField')(default=datetime.date(2011, 8, 1), max_length=100))

    models = {
        'story.image': {
            'Meta': {'object_name': 'Image'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        'story.media': {
            'Meta': {'object_name': 'Media'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
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
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story.Image']", 'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['story.Media']", 'null': 'True', 'blank': 'True'}),
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
