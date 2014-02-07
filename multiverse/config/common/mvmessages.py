#
#
#  The Multiverse Platform is made available under the MIT License.
#
#  Copyright (c) 2012 The Multiverse Foundation
#
#  Permission is hereby granted, free of charge, to any person 
#  obtaining a copy of this software and associated documentation 
#  files (the "Software"), to deal in the Software without restriction, 
#  including without limitation the rights to use, copy, modify, 
#  merge, publish, distribute, sublicense, and/or sell copies 
#  of the Software, and to permit persons to whom the Software 
#  is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be 
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
#  OR OTHER DEALINGS IN THE SOFTWARE.
#
#  

import sys
from java.util import *
from java.lang import *
from multiverse.mars.plugins import *
from multiverse.msgsys import *
from multiverse.management import Management
from multiverse.server.math import *
from multiverse.server.plugins import *
from multiverse.server.util import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.messages import PropertyMessage
from multiverse.server.messages import LoginMessage
from multiverse.server.messages import LogoutMessage
from multiverse.server.messages import SearchMessage

# This config file defines the catalog of message types used by the
# multiverse system.  All server plugins load this file during startup
# before _any_ message is sent, and thus can agree on the generated
# message numbers.

# Game developers can extend the list of cataloged messages by adding
# to the file config/world_name/worldmessages.py.  The startup script
# multiverse.sh ensures that both mvmessages.py and
# config/world_name/worldmessages.py are read by every plugin before
# any messages are generated

# Create the Multiverse message catalog

mvMessageCatalog = MessageCatalog.addMsgCatalog("mvMessageCatalog", 1, 500);

# PropertyMessage
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, PropertyMessage.MSG_TYPE_PROPERTY)

# LoginMessage
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, LoginMessage.MSG_TYPE_LOGIN)

# LogoutMessage
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, LogoutMessage.MSG_TYPE_LOGOUT)

# Add the WorldManagerClient messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_ANIMATION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_COM)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_COM_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_DC_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_DESPAWNED)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_DESPAWN_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_DETACH)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_DIR_LOC_ORIENT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_DISPLAY_CONTEXT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_EXTENSION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_FOG)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_FREE_REMOTE_OBJ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_GETWNODE_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_MOB_PATH)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_MOB_PATH_CORRECTION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_MOB_PATH_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_MODIFY_DC)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_NEW_DIRLIGHT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_FREE_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_NEW_REGION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_NEW_REMOTE_OBJ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_OBJINFO_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_ORIENT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_ORIENT_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_PERCEIVER_REGIONS)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_REFRESH_WNODE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_REPARENT_WNODE_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_ROAD)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_FREE_ROAD)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_SETWNODE_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_SET_AMBIENT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_SOUND)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_SPAWNED)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_SPAWN_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_SYS_CHAT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_TARGETED_PROPERTY)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_UPDATEWNODE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_UPDATEWNODE_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_UPDATE_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_WNODECORRECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_P2P_EXTENSION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_PERCEPTION_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_PERCEPTION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_HOST_INSTANCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, WorldManagerClient.MSG_TYPE_PLAYER_PATH_WM_REQ)

# Add the messages for the ObjectManager

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_SET_PERSISTENCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_SET_SUBPERSISTENCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_LOAD_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_LOAD_SUBOBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_LOAD_OBJECT_DATA)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_SAVE_OBJECT_DATA)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_SAVE_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_SAVE_SUBOBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_GENERATE_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_GENERATE_SUB_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_SUB_OBJECT_DEPS_READY)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_REGISTER_TEMPLATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_GET_TEMPLATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_GET_TEMPLATE_NAMES)

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_UNLOAD_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_UNLOAD_SUBOBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_DELETE_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_DELETE_SUBOBJECT)

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_FIX_WNODE_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_GET_NAMED_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectManagerClient.MSG_TYPE_GET_OBJECT_STATUS)

# Add InventoryClient messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_ADD_ITEM)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_CREATE_INV)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_INV_UPDATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_ACTIVATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_LOOTALL)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_INV_FIND)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_INV_REMOVE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InventoryClient.MSG_TYPE_DESTROY_ITEM)


# Add ObjectTracker message

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ObjectTracker.MSG_TYPE_NOTIFY_REACTION_RADIUS)

# Add EnginePlugin messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, EnginePlugin.MSG_TYPE_DUMP_ALL_THREAD_STACKS)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, EnginePlugin.MSG_TYPE_GET_PROPERTY)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, EnginePlugin.MSG_TYPE_PLUGIN_STATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, EnginePlugin.MSG_TYPE_SET_PROPERTY)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, EnginePlugin.MSG_TYPE_SET_PROPERTY_NONBLOCK)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, EnginePlugin.MSG_TYPE_TRANSFER_OBJECT)

# Add Behavior messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, Behavior.MSG_TYPE_COMMAND)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, Behavior.MSG_TYPE_EVENT)

# Add Quest messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_REQ_QUEST_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_REQ_CONCLUDE_QUEST)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_QUEST_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_GET_QUEST_STATUS)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_QUEST_RESP)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_NEW_QUESTSTATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_CONCLUDE_QUEST)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_QUEST_STATE_STATUS_CHANGE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_QUEST_LOG_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_QUEST_STATE_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_REMOVE_QUEST_RESP)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, QuestClient.MSG_TYPE_REQ_RESET_QUESTS)

# Add MarsInventory message

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_MARS_INV_FIND)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_TRADE_START_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_TRADE_START)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_TRADE_COMPLETE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_TRADE_OFFER_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_TRADE_OFFER_UPDATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MarsInventoryClient.MSG_TYPE_SWAP_ITEM)

# Add CombatClient messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_AUTO_ATTACK)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_START_ABILITY)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_COOLDOWN)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_ABILITY_PROGRESS)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_DAMAGE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_RELEASE_OBJECT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_ABILITY_UPDATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_ADD_SKILL)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_TRAINING_FAILED)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_COMBAT_ABILITY_MISSED)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, CombatClient.MSG_TYPE_SKILL_UPDATE)

# Add AnimationClient messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, AnimationClient.MSG_TYPE_INVOKE_EFFECT)

# Add InstanceClient messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_REGISTER_INSTANCE_TEMPLATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_CREATE_INSTANCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_GET_INSTANCE_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_INSTANCE_ENTRY_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_GET_MARKER)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_GET_REGION)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_LOAD_INSTANCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_UNLOAD_INSTANCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_DELETE_INSTANCE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_LOAD_INSTANCE_CONTENT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_INSTANCE_UNLOADED)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, InstanceClient.MSG_TYPE_INSTANCE_DELETED)

# mob manager (temporary)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, MobManagerClient.MSG_TYPE_CREATE_SPAWN_GEN)

# Add Proxy messages
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_VOICE_PARMS)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_PLAYER_PATH_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_UPDATE_PLAYER_IGNORE_LIST)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_RELAY_UPDATE_PLAYER_IGNORE_LIST)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_GET_MATCHING_PLAYERS)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_PLAYER_IGNORE_LIST)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_PLAYER_IGNORE_LIST_REQ)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ProxyPlugin.MSG_TYPE_GET_PLAYER_LOGIN_STATUS)

# Search messages
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, SearchMessage.MSG_TYPE_SEARCH);

# Add TrainerClient messages

MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, TrainerClient.MSG_TYPE_REQ_TRAINER_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, TrainerClient.MSG_TYPE_REQ_SKILL_TRAINING)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, TrainerClient.MSG_TYPE_TRAINING_INFO)

# Add ClassAbilityClient Messages
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ClassAbilityClient.MSG_TYPE_STAT_XP_UPDATE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, ClassAbilityClient.MSG_TYPE_HANDLE_EXP)

#Add GroupClient messages
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_INVITE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_INVITE_RESPONSE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_REMOVE_MEMBER)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_CHAT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_REQUEST_GROUP_INFO)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_INFO_RESPONSE)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_SET_ALLOWED_SPEAKER)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_MUTE_VOICE_CHAT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, GroupClient.MSG_TYPE_GROUP_VOICE_CHAT_STATUS)

#Add VoiceClient messages
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, VoiceClient.MSG_TYPE_VOICECLIENT)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, VoiceClient.MSG_TYPE_VOICE_MEMBER_ADDED)
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, VoiceClient.MSG_TYPE_VOICE_MEMBER_REMOVED)

# multiverse.management
MessageCatalog.addMsgTypeTranslation(mvMessageCatalog, Management.MSG_TYPE_GET_PLUGIN_STATUS)

